#!/usr/bin/env python3
"""
Simple CV Management System for Odoo
Three core functions: check_positions, add_cvs, show_uploads
"""

import os
import xmlrpc.client
import base64
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Odoo connection settings from environment variables
ODOO_URL = os.getenv('ODOO_URL', 'http://localhost:8069')
ODOO_DB = os.getenv('ODOO_DB', 'test')
ODOO_USERNAME = os.getenv('ODOO_USERNAME')
ODOO_PASSWORD = os.getenv('ODOO_PASSWORD')

def _connect_to_odoo():
    """Internal function to connect to Odoo"""
    try:
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        if uid:
            models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
            return uid, models
        return None, None
    except Exception as e:
        print(f"❌ Error connecting to Odoo: {e}")
        return None, None

def check_positions():
    """Returns all open job positions"""
    uid, models = _connect_to_odoo()
    if not uid:
        return []

    try:
        positions = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'hr.job', 'search_read', [[]], {'fields': ['name', 'id']})
        return [(pos['id'], pos['name']) for pos in positions]
    except Exception as e:
        print(f"❌ Error fetching positions: {e}")
        return []

def add_cvs(cv_path, position):
    """Adds a single CV to the specified position"""
    uid, models = _connect_to_odoo()
    if not uid:
        return False

    if not os.path.exists(cv_path):
        print(f"❌ CV file not found: {cv_path}")
        return False

    try:
        # Read and encode CV file
        with open(cv_path, 'rb') as f:
            file_data = base64.b64encode(f.read()).decode('utf-8')

        # Extract applicant name from filename
        filename = os.path.basename(cv_path)
        applicant_name = os.path.splitext(filename)[0].replace('_', ' ')

        # Find job position by name
        job_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'hr.job', 'search', [[('name', '=', position)]])

        if not job_ids:
            print(f"❌ Position '{position}' not found")
            return False

        job_id = job_ids[0]

        # Create applicant record
        applicant_data = {
            'name': applicant_name,
            'partner_name': applicant_name,
            'job_id': job_id,
            'email_from': f"{applicant_name.lower().replace(' ', '.')}@example.com",
            'description': f'CV uploaded: {filename}',
        }

        applicant_id = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'hr.applicant', 'create', [applicant_data])

        # Attach CV file
        attachment_data = {
            'name': filename,
            'type': 'binary',
            'datas': file_data,
            'res_model': 'hr.applicant',
            'res_id': applicant_id,
            'mimetype': 'application/pdf' if filename.lower().endswith('.pdf') else 'application/msword'
        }

        models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'ir.attachment', 'create', [attachment_data])

        print(f"✅ Added {applicant_name} to {position}")
        return True

    except Exception as e:
        print(f"❌ Error adding CV: {e}")
        return False

def show_uploads():
    """Shows all uploaded CVs and their positions"""
    uid, models = _connect_to_odoo()
    if not uid:
        return []

    try:
        applicants = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'hr.applicant', 'search_read', [[]],
            {'fields': ['name', 'job_id', 'email_from', 'create_date']})

        uploads = []
        for applicant in applicants:
            job_name = applicant['job_id'][1] if applicant['job_id'] else 'No Position'
            uploads.append({
                'name': applicant['name'],
                'position': job_name,
                'email': applicant['email_from'],
                'date': applicant['create_date']
            })

        return uploads

    except Exception as e:
        print(f"❌ Error fetching uploads: {e}")
        return []
