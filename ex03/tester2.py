from new_student import Student
# Crear una instancia de Student
student1 = Student(name="John", surname="Doe")

# Ver la representación del objeto
print(student1)  # Esto es generado automáticamente por el decorador @dataclass

# Acceder a los atributos
print(student1.name)     # John
print(student1.surname)  # Doe
print(student1.active)   # True
print(student1.login)    # JDoe
print(student1.id)       # ID aleatorio generado automáticamente (e.g., xjkdovwzxtuqlgfr)
