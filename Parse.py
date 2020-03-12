"""
imports Spacy, OS, Pandas, NLTK.
To parse the objects for their skills and work experiences.
"""
from Load import Load


class Parse:

    def __init__(self):
        self.L = Load()

    # @staticmethod
    def getCity(self):
        L = Load()
        city = L.load_skills('../Dataset/Lists/city_list.txt')
        return city

    # @staticmethod
    def getState(self):
        L = Load()
        state = L.load_skills('../Dataset/Lists/State_list.txt')
        return state

    # @staticmethod
    def getSkills(self):
        L = Load()
        skills = L.load_skills('../Dataset/Lists/skills_list.txt')
        return skills

    # @staticmethod
    def getReskey(self):
        L = Load()
        reskey = L.load_skills('../Dataset/Lists/resume_keywords_clean.txt')
        return reskey

    # @staticmethod
    def getResume(self):
        L = Load()
        df = L.imports('../Dataset/Profiles/Resume_1.json')
        data = L.get_data(df)








