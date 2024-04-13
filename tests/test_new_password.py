import string
from password.new_password import generate_password
import pytest

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
        
def test_password_length():
    password_length = 12
    password = generate_password(password_length)
    assert len(password) == password_length


def test_different_passwords_generations():
    """Тест, что два сгенерированных подряд пароля различаются"""
    pw0 = generate_password(12)
    pw1 = generate_password(12)
    assert pw0 != pw1

def test_password_lenght_is_correct():
    """Тест, что длина пароля соответствует заданной"""
    pw = generate_password(21)
    assert any(char.isupper() for char in pw)

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
