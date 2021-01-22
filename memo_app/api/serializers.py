from rest_framework import serializers

from memo_app.models import Note


class NoteSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Note
        fields = ['id', 'note_subject', 'note_body', 'pub_date', 'username']
        extra_kwargs = {
            'pub_date': {'read_only': True}
        }

    def get_username_from_author(self, note):
        username = note.author.username
        return username


