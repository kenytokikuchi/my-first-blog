from django.contrib import admin
from .models import Post

# 作成したポストを追加、編集、削除はこのファイル
admin.site.register(Post) # モデルをadminページで見れるように設定
