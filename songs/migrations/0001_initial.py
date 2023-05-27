
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='album_covers')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='artist_photos')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('audio_file', models.FileField(upload_to='songs')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.album')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='songs.genre')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.artist'),
        ),
    ]
