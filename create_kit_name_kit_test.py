import sender_stand_request
import data
from data import user_body


def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = kit_name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    positive_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()['name'] == kit_name

def negative_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    negative_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert negative_kit_response.status_code == 400
    assert negative_kit_response.json()['code'] == 4000

def test_caracter_1():
    positive_assert("a")

def test_caracteres_511():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_0_caracteres():
    negative_assert("")

def test_caracteres_512():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_numero_caracteres_especiales_permitidos_():
    positive_assert("\"№%@\",")

def test_espacios_permitidos():
    positive_assert("A Aaa")

def test_numeros_permitidos():
    positive_assert("123")

def test_el_parametro_no_se_pasa_en_la_solicitud():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

def test_parametro_diferente_ha_sido_aceptado():
    negative_assert(123)