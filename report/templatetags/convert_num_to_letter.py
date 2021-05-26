from django import template


register = template.Library()


lst_string_nums = [
    'one', 'two', 'three',
    'four', 'five', 'six',
    'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve',
    'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen',
    'nineteen', 'twenty'
]

@register.filter
def convert_num_to_letter(number):
    if number in range(1, 21):
        number = lst_string_nums[number - 1]
        return number




