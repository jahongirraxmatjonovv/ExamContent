from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Test

def test_view(request):
    tests = Test.objects.all()
    return render(request, 'calc.html', {'tests':tests})

@require_POST
def result_view(request):
    tests = Test.objects.all()
    count = 0
    for test in tests:
        try:
            if test.correct == request.POST[test.question]:
                count += 1
        except:
            return HttpResponse('Siz barcha muammolarni hal qilishingiz kerak')
    return render(request, 'result.html', {'hisoblash':count, 'hammasi':(tests.count()-count)})