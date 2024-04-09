import subprocess
import os

# Získanie cesty k aktuálnemu skriptu
current_script_path = os.path.abspath(__file__)

# Získanie adresára nadradeného o dve úrovne
parent_directory = os.path.abspath(os.path.join(current_script_path, os.pardir))

# Skripty pre IT_CUSTOMER_CHURN
scripts_to_run_ITCUSTOMERCHRUN = [
    'noise_reduction/ADASYN.py',
    'noise_reduction/BorderlineSMOTE.py',
    'noise_reduction/none.py',
    'noise_reduction/SMOTE.py',
    'without_noise_reduction/ADASYN.py',
    'without_noise_reduction/BorderlineSMOTE.py',
    'without_noise_reduction/none.py',
    'without_noise_reduction/SMOTE.py',
]

base_directory_ITCUSTOMERCHRUN = os.path.join(parent_directory, 'IT_Customer_Chrun')
# print(base_directory_ITCUSTOMERCHRUN)

for script_path in scripts_to_run_ITCUSTOMERCHRUN:
    # Získajte plnú cestu k súboru
    file_to_run_ITCUSTOMERCHRUN = os.path.abspath(os.path.join(base_directory_ITCUSTOMERCHRUN, script_path))

    # Získajte pracovný adresár zo súboru
    working_directory_ITCUSTOMERCHRUN = os.path.dirname(file_to_run_ITCUSTOMERCHRUN)

    try:
        # Nastavte pracovný adresár na adresár so skriptom
        os.chdir(working_directory_ITCUSTOMERCHRUN)

        # Spustite súbor
        subprocess.run(['python', file_to_run_ITCUSTOMERCHRUN])

    except FileNotFoundError:
        print(f"Súbor nebol nájdený: {file_to_run_ITCUSTOMERCHRUN}")


# --------------------------------------------------------------------------------------------------------------------

# Skripty pre BANK_FRAUDS
scripts_to_run_BANKFRAUDS = [
    'noise_reduction/ADASYN.py',
    'noise_reduction/BorderlineSMOTE.py',
    'noise_reduction/none.py',
    'noise_reduction/SMOTE.py',
    'without_noise_reduction/ADASYN.py',
    'without_noise_reduction/BorderlineSMOTE.py',
    'without_noise_reduction/none.py',
    'without_noise_reduction/SMOTE.py',
]

base_directory_BANKFRAUDS = os.path.join(parent_directory, 'Bank_Frauds')
# print(base_directory_BANKFRAUDS)

for script_path in scripts_to_run_BANKFRAUDS:
    # Získajte plnú cestu k súboru
    file_to_run_BANKFRAUDS = os.path.abspath(os.path.join(base_directory_BANKFRAUDS, script_path))

    # Získajte pracovný adresár zo súboru
    working_directory_BANKFRAUDS = os.path.dirname(file_to_run_BANKFRAUDS)

    try:
        # Nastavte pracovný adresár na adresár so skriptom
        os.chdir(working_directory_BANKFRAUDS)

        # Spustite súbor
        subprocess.run(['python', file_to_run_BANKFRAUDS])

    except FileNotFoundError:
        print(f"Súbor nebol nájdený: {file_to_run_BANKFRAUDS}")

# --------------------------------------------------------------------------------------------------------------------

# Skripty pre HEARTDISEASE
scripts_to_run_HEARTDISEASE = [
    'noise_reduction/ADASYN.py',
    'noise_reduction/BorderlineSMOTE.py',
    'noise_reduction/none.py',
    'noise_reduction/SMOTE.py',
    'without_noise_reduction/ADASYN.py',
    'without_noise_reduction/BorderlineSMOTE.py',
    'without_noise_reduction/none.py',
    'without_noise_reduction/SMOTE.py',
]

base_directory_HEARTDISEASE = os.path.join(parent_directory, 'Heart_Disease')
# print(base_directory_HEARTDISEASE)

for script_path in scripts_to_run_HEARTDISEASE:
    # Získajte plnú cestu k súboru
    file_to_run_HEARTDISEASE = os.path.abspath(os.path.join(base_directory_HEARTDISEASE, script_path))

    # Získajte pracovný adresár zo súboru
    working_directory_HEARTDISEASE = os.path.dirname(file_to_run_HEARTDISEASE)

    try:
        # Nastavte pracovný adresár na adresár so skriptom
        os.chdir(working_directory_HEARTDISEASE)

        # Spustite súbor
        subprocess.run(['python', file_to_run_HEARTDISEASE])

    except FileNotFoundError:
        print(f"Súbor nebol nájdený: {file_to_run_HEARTDISEASE}")
