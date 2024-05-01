
from django.urls import path

from django.contrib import admin
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from.forms import LoginForm,MyPasswordResetFrom,MyPasswordChangeForm,MySetPasswordFrom


urlpatterns = [
    path('', views.home),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('category/<slug:val>', views.Category.as_view(),name='category'),
    path('category-title/<val>', views.CategoryTitle.as_view(),name='category-title'),
    path('product-details/<int:pk>/', views.ProductDetail.as_view(),name='product-detail'),
    path('profile/',views.ProfileView.as_view(), name='profile'),
    path('address/',views.address, name='address'),
    path('updateaddress/<int:pk>',views.UpdateAddress.as_view(), name='updateaddress'),

    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('paymentdone/',views.payment_done,name='paymentdone'),
    path('orders/',views.orders,name='orders'),
    path('showwishlist/',views.show_wishlist,name='showwishlist'),

    path('search/',views.search,name='search'),
    
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    path('pluswishlist/',views.plus_wishlist,name='pluswishlist'),
    path('minuswishlist/',views.minus_wishlist,name='minuswishlist'),


    #login Auth
    path('rejistration/',views.CustomerRejistrationView.as_view(),
    name='customerrejistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name=
    'app/login.html',form_class=LoginForm), name='login'),

    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name=
    'app/changepassword.html',form_class=MyPasswordChangeForm, success_url=
    '/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    #Important Urls

    path('password-reset',auth_view.PasswordResetView.as_view
    (template_name='app/password_reset.html'),name='password_reset'),

    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view
    (template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view
    (template_name='app/password_reset_confirm.html',form_class=MySetPasswordFrom),name='password_reset_confirm'),

    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view
    (template_name='app/password_reset_complete.html'),name='password_reset_complete'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Ramu Dairy"
admin.site.site_title="Ramu Dairy"
admin.site.site_index_title = "Welcome to Ramu Dairy Shop"

