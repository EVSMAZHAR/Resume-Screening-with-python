from nltk.corpus import stopwords

# Muhammad Mazhar
NAME_PATTERN = [{'POS': 'PROPN'}, {'POS': 'PROPN'},{"ORTH": "User"}, {"ORTH": "name"}, {"ORTH": ":"}, {}]

# Education (Upper Case Mandatory)
EDUCATION = [
            'BSC','BS Computer Science', 'BSCS', 'BSIT', 'BS Information technologies', 'BSSE','BS Software Engineering', 'BBIT', 'BSDS','MSDS','MSC', 'MSCS', 'Pre-engineering','Aeronautics and Aviation Science','Anthropology','Art','Business Administration','Chemistry','Economics','Education','Engineering','Literature','Law','Nursing and Health Sciences','Medical and Dental Sciences','Pharmacy','Physical Science','Engineering','Integrated Science','Sociology','Social Welfare','Tourism Studies','Media Studies','International Relations','Engineering','Nursing Science','Medical Technology','Health Sciences','Medicine','Pharmacy','Mathematics','Biology','General Science','Mechanical Engineering','Biotechnology','Industrial Design',
            'MCS', 'MS', 'M.S', 'BTECH', 'MTECH','PHD','MPHIL','ICS' ,'FSC','ICOM','BCOM','DCOM','Information Engineering','Agriculture','Agricultural Engineering','Fisheries Science','Forest Science','Veterinary Medicine','Animal Science','Agricultural Chemistry','Fashion','Music',''
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII','intermediate','school']

NOT_ALPHA_NUMERIC = r'[^a-zA-Z\d]'

NUMBER = r'\d+'

# For finding date ranges
MONTHS_SHORT = r'''(jan)|(feb)|(mar)|(apr)|(may)|(jun)|(jul)
                   |(aug)|(sep)|(oct)|(nov)|(dec)'''
MONTHS_LONG = r'''(january)|(february)|(march)|(april)|(may)|(june)|(july)|
                   (august)|(september)|(october)|(november)|(december)'''
MONTH = r'(' + MONTHS_SHORT + r'|' + MONTHS_LONG + r')'
YEAR = r'(((20|19)(\d{2})))'

STOPWORDS = set(stopwords.words('english'))

RESUME_SECTIONS_PROFESSIONAL = [
                    'experience',
                    'education',
                    'interests',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]

RESUME_SECTIONS_GRAD = [
                    'accomplishments',
                    'experience',
                    'education',
                    'interests',
                    'projects',
                    'professional experience',
                    'publications',
                    'skills',
                    'certifications',
                    'objective',
                    'career objective',
                    'summary',
                    'leadership'
                ]
terms = {'Quality/Six Sigma':['black belt','capability analysis','control charts','doe','dmaic','fishbone',
                              'gage r&r', 'green belt','ishikawa','iso','kaizen','kpi','lean','metrics',
                              'pdsa','performance improvement','process improvement','quality',
                              'quality circles','quality tools','root cause','six sigma',
                              'stability analysis','statistical analysis','tqm'],      
        'Operations management':['automation','bottleneck','constraints','cycle time','efficiency','fmea',
                                 'machinery','maintenance','manufacture','line balancing','oee','operations',
                                 'operations research','optimization','overall equipment effectiveness',
                                 'pfmea','process','process mapping','production','resources','safety',
                                 'stoppage','value stream mapping','utilization'],
        'Supply chain':['abc analysis','apics','customer','customs','delivery','distribution','eoq','epq',
                        'fleet','forecast','inventory','logistic','materials','outsourcing','procurement',
                        'reorder point','rout','safety stock','scheduling','shipping','stock','suppliers',
                        'third party logistics','transport','transportation','traffic','supply chain',
                        'vendor','warehouse','wip','work in progress'],
        'Project management':['administration','agile','budget','cost','direction','feasibility analysis',
                              'finance','kanban','leader','leadership','management','milestones','planning',
                              'pmi','pmp','problem','project','risk','schedule','scrum','stakeholders'],
        'Data analytics':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining',
                          'visualuzation','communication','storytelling','collaboration'],
         'Data Science':['analytics','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','hadoop platform','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining',
                          'visualuzation','Learning','communication','storytelling','collaboration'],
         'Machine Learning':['analytics','api','aws','big data','busines intelligence','clustering','code',
                          'coding','data','database','data mining','data science','deep learning','hadoop',
                          'hypothesis test','iot','internet','machine learning','modeling','nosql','nlp',
                          'predictive','programming','python','r','sql','tableau','text mining',
                          'visualuzation'],
         'Software Engineernig':['api','aws','azure','coding','database','hypothesis test','iot','internet', 
                                 'programming','python','r','OOP','object oriented programming','test','c#','java','web development','.net','asp.net','ror','php','linq','javascript','agile','sdlc','logical thinking','problem solving','algorathims','data structure','web programming','html','css','bootstrap','teamwork'],
                 'Network Engineerning':['firewall','security','networking','cloud computing','warehousing','operating system','commmunication skills','coding','problem solving','trubleshooting','man','pan','lan','voip',
                          'san','wan','internet','can','wlan','gan','cisco',
                          'switching','routing','python','security','iot',],
        'Healthcare':['adverse events','care','clinic','cphq','ergonomics','healthcare',
                      'health care','health','hospital','human factors','medical','near misses',
                      'patient','reporting system']}
