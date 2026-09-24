class UniversityConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            #Default configuration
            cls._instance.university_name = None
            cls._instance.academic_year = None
            cls._instance.semester = None
        return cls._instance
    def set_config(self,university_name,academic_year,semester):
        self.university_name = university_name
        self.academic_year = academic_year
        self.semester = semester
    def display_config(self):
        print("University Name:", self.university_name)
        print("Academic Year:", self.academic_year)
        print("Semester:", self.semester)
# Create three objects
config1 = UniversityConfig()
config2 = UniversityConfig()
config3 = UniversityConfig()
# Set configuration using config1
config1.set_config(
    "Brac University",
    "2026",
    "Semester 08"
)
# Display configuration using config2
config2.display_config()
# Check whether they are the same object
print("config1 and config2 are same:", config1 is config2)
print("config2 and config3 are same:", config2 is config3)
print("config1 and config3 are same:", config1 is config3)
