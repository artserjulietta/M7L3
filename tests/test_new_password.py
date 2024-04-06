import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_different_generated_passwords():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2

"""# Тест, что пароль содержит хотя бы одну букву в верхнем регистре
def test_contains_uppercase_letter():
    Тест, что пароль содержит хотя бы одну букву в верхнем регистре
    password = generate_password(20)
    assert any(char.isupper() for char in password)"""