from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from .views import *

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('api/getlogos', logo_api, name='logo-api'),
    path('api/login', login_api, name='login-api'),
    path('api/getrecipientbyid_deleteorpatch/<int:id>', get_recipient_by_id_delete_patch, name='recipient-by-id'),
    path('api/getrecipientchildren/<int:id>', get_recipient_children, name='recipient-children'),
    path('api/getrecipientchildbyid_updateordelete/<int:recipient_id>/<int:child_id>', get_recipient_child_by_id_update_delete, name='child-by-id'),
    path('api/getallmustpays', get_all_must_pays, name='all-mustpays'),
    path('api/getmustpaybyid_deleteorpatch/<int:id>', get_mustpay_by_id_patch_delete, name='get-patch-delete-mustpay-by-id'),
    path('api/mustpayreceipts/<int:id>', get_mustpay_receipts, name='all-mustpay-receipts'),
    path('api/mustpayreceiptsbyid_deleteorpatch/<int:mustpay_id>/<int:receipt_id>', get_receipt__by_id_update_delete, name='configure-receipt-by-id'),
    path('api/getinsolvents', InsolventsSinceThreeMonths.as_view(), name='insolvent-api'),
    path('api/getallalimonies', AlimonyList.as_view(), name='all-alimonies')
]
