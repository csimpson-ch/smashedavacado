from django.urls import path
from . import views
from .views import *

app_name = "mortgage"
urlpatterns = [
    # path('', views.index, name="index"),
    # path('login/', views.user_login, name='login'),
    # path('signup/', views.user_signup, name='signup'),
    # path('logout/', views.user_logout, name='logout'),
    # path('blog/', BlogPostListView.as_view(), name='blog_list'),
    # path('blog/create', views.blog_create, name='blog_create'),
    # path('blog/<int:blogpost_id>/delete', views.blog_delete, name='blog_delete'),
    # path('blog/<int:blogpost_id>/edit', views.blog_edit, name='blog_edit'),
    # path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
    # path('create/', views.create, name='create'),
    # path('for_approval/<error>', views.for_approval, name='for_approval'),
    # # path('for_approval/', views.for_approval_with_error, name='for_approval_with_error'),
    # path('generate_transactions/', views.generate_transactions, name='generate_transactions'),
    # path('loans/', LoanListView.as_view(), name='loan_list'),
    # path('loans/create/', views.loan_create, name='loan_create'),
    # path('loans/<int:loan_id>/payment', views.loan_payment, name='loan_payment'),
    # # path('loans/<int:loan_id>/detail', views.loan_detail, name='loan_detail'),
    # path('loans/<int:loan_id>/delete', views.loan_delete, name='loan_delete'),
    # path('loans/<int:loan_id>/edit', views.loan_edit, name='loan_edit'),
    # path('expenseinterval/', ExpenseIntervalListView.as_view(), name='expenseinterval_list'),
    # path('expenseinterval/create/', views.expenseinterval_create, name='expenseinterval_create'),
    # path('expenseinterval/<int:expenseinterval_id>/details', views.expenseinterval_details, name='expenseinterval_details'),
    # path('expenseinterval/<int:expenseinterval_id>/delete', views.expenseinterval_delete, name='expenseinterval_delete'),
    # path('expenseinterval/<int:expenseinterval_id>/edit', views.expenseinterval_edit, name='expenseinterval_edit'),
    # path('expenseadhoc/', ExpenseAdhocListView.as_view(), name='expenseadhoc_list'),
    # path('expenseadhoc/create/', views.expenseadhoc_create, name='expenseadhoc_create'),
    # # path('expenseadhoc/approve_all', views.expenseadhoc_approve_all, name='expenseadhoc_approve_all'),
    # path('expenseadhoc/<int:expenseadhoc_id>/approve', views.expenseadhoc_approve, name='expenseadhoc_approve'),
    # path('expenseadhoc/<int:expenseadhoc_id>/delete', views.expenseadhoc_delete, name='expenseadhoc_delete'),
    # path('expenseadhoc/<int:expenseadhoc_id>/edit', views.expenseadhoc_edit, name='expenseadhoc_edit'),
    # path('backend_get_all_blogposts/', views.backend_get_all_blogposts, name='backend_get_all_blogposts'),
]