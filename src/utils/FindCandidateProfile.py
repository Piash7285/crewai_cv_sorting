import os


def get_candidate():
    cvs_folder = os.path.join(os.getcwd(), 'cvs')
    linkedin_folder = os.path.join(os.getcwd(), 'linkedin_pdfs')
    print(60 * "-")
    print("Searching for CV and LinkedIn PDF files...")
    all_profiles = []

    # Find all CV files and their corresponding LinkedIn PDFs
    if os.path.exists(cvs_folder):
        for cv in os.listdir(cvs_folder):
            if cv.endswith('.pdf'):
                cv_path = os.path.abspath(os.path.join(cvs_folder, cv))

                # Look for corresponding LinkedIn PDF with the same name
                linkedin_path = os.path.join(linkedin_folder, cv)
                if os.path.exists(linkedin_path):
                    linkedin_path = os.path.abspath(linkedin_path)
                    profiles = {
                        'cv_path': cv_path,
                        'linkedin_path': linkedin_path
                    }
                    all_profiles.append(profiles)
                    print(60* "-")
                    print(f"cv path:{cv_path}\nlinkedin path:{linkedin_path}")
                else:
                    print(60 * "-")
                    print(f"cv path:{cv_path}\nNo LinkedIn profile found")

    if all_profiles:
        print(60 * "-")
        print(f"Total profiles found: {len(all_profiles)}")
        return all_profiles
    else:
        print(60 * "-")
        print("No matching CV and LinkedIn pairs found")
        return []
