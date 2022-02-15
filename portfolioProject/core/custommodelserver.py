from .models import Header, Footer

def headfoot(request):
    headerr = Header.objects.last()
    # footerr = Footer.objects.last()
    # all stuff that you want to make available
    context = {
        'headerr':headerr,
        # 'footerr':footerr
    }
    return context
