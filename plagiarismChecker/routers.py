from rest_framework.routers import DefaultRouter
from .views import PlagiarismCheckerView

router = DefaultRouter()
router.register(r'plagiarism-checker', PlagiarismCheckerView, basename='plagiarism-checker')
