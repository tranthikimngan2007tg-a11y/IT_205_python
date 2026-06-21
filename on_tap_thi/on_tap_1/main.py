class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practice_score = practice_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = "Chưa cập nhật"

    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def theory_score(self):
        return self.__theory_score
    @property
    def practice_score(self):
        return self.__practice_score
    @property
    def project_score(self):
        return self.__project_score
    @property
    def final_score(self):
        return self.__final_score
    @property
    def academic_rank(self):
        return self.__academic_rank
    
    def update_theory_score(self, theory_score):
        self.__theory_score = theory_score
    def update_practice_score(self, practice_score):
        self.__practice_score = practice_score
    def update_project_score(self, project_score):
        self.__project_score = project_score
    
    def calculate_final_score(self):
        self.__final_score = (self.__theory_score * 0.2) + (self.__practice_score * 0.3) +(self.project_score * 0.5)
    def classify_academic_rank(self):
        if self.__final_score < 0 or self.__final_score > 10:
            print("Điểm không hợp lệ!")
            return
        if self.__final_score >= 8.5:
            self.__academic_rank = "Giỏi"
        elif self.__final_score >= 7:
            self.__academic_rank = "Khá"
        elif self.final_score >= 5:
            self.__academic_rank = "Trung bình"
        else:
            self.__academic_rank = "Yếu"



        