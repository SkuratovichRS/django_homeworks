from rest_framework.exceptions import APIException


class PostAdvForbidden(APIException):
    status_code = 403
    default_detail = "Вы не можете разместить больше 10-ти открытых объявлений"
