FTP_DATA_SUFFIX = "csv"
FTP_ROOT_DIRECTORY = r"C:/Code/Test"

TREATMENT_DOCUMENT_TYPE = "treatment"
PATIENT_DOCUMENT_TYPE = "document"

MongoAddr = ""

MAIN_LOOP_TIME_INTERVAL = 60
BULK_NORAMLIZED_DATA_SIZE = 1000

ABBREV_TO_STATE = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
                   'CO': 'Colorado',
                   'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida',
                   'GA': 'Georgia', 'HI': 'Hawaii',
                   'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa', 'KS': 'Kansas', 'KY': 'Kentucky',
                   'LA': 'Louisiana',
                   'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota',
                   'MS': 'Mississippi',
                   'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire',
                   'NJ': 'New Jersey',
                   'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota',
                   'MP': 'Northern Mariana Islands',
                   'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PW': 'Palau', 'PA': 'Pennsylvania',
                   'PR': 'Puerto Rico',
                   'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas',
                   'UT': 'Utah',
                   'VT': 'Vermont', 'VI': 'Virgin Islands', 'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia',
                   'WI': 'Wisconsin', 'WY': 'Wyoming'}


class PatientFormatConfig:
    PATIENT_ID = "patient_id"
    MRN = "mrn"
    DATE_OF_BIRTH = "date_of_birth"
    IS_DECEASED = "is_deceased"
    DATE_OF_DEATH = "date_of_death"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    GENDER = "gender"
    SEX = "sex"
    STREET_ADDRESS = "street_address"
    CITY = "city"
    STATE = "state"
    ZIP_CODE = "zip_code"


class TreatmentFormatConfig:
    pass
