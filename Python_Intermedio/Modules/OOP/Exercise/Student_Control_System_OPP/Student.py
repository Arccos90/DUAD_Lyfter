class Student:
    def __init__(self, id_student, student_name: str, last_name: str, second_surname: str, class_type: str, spanish: float, english: float, socials: float, science: float, avg_note: float = None):
        self.id = int(id_student)
        self.student_name = student_name
        self.last_name = last_name
        self.second_surname = second_surname
        self.type = class_type
        self.spanish = float(spanish)
        self.english = float(english)
        self.socials = float(socials)
        self.science = float(science)
        self.avg_note = float(avg_note) if avg_note is not None else self.calculate_average()

    def calculate_average(self):
        return (self.spanish + self.english + self.socials + self.science) / 4

    @classmethod
    def from_csv_row(cls, row):
        """Convierte un diccionario leído del CSV en una instancia de Student."""
        return cls(
            id_student=row['ID'],
            student_name=row['student_name'],
            last_name=row['last_name'],
            second_surname=row['second_surname'],
            class_type=row['type'],
            spanish=row['spanish'],
            english=row['english'],
            socials=row['socials'],
            science=row['science'],
            avg_note=row.get('avg_note')
        )

    def to_dict(self):
        """Convierte los atributos del objeto a formato diccionario para CSV."""
        return {
            'ID': self.id,
            'student_name': self.student_name,
            'last_name': self.last_name,
            'second_surname': self.second_surname,
            'type': self.type,
            'spanish': self.spanish,
            'english': self.english,
            'socials': self.socials,
            'science': self.science,
            'avg_note': self.avg_note
        }