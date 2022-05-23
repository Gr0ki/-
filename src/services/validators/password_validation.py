from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SymbolRepetitionValidator:
    def validate(self, password, user=None):
        if len(tuple(password)) != len(set(password)):
            raise ValidationError(
                _("Your password mustn't contain duplicate characters!"),
                code='password_symbol_repetition',
            )

    def get_help_text(self):
        return _("Your password mustn't contain duplicate characters!")
