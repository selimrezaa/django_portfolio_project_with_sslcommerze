from second_app.models import Footer

def footer(request):
    footer = Footer.objects.last()
    # all stuff that you want to make available
    context = {
        'footer':footer
    }
    return context
