from rest_framework import serializers



class question_serializer(serializers.Serializers):

    class Meta:
        model = myapp.models.Question



    def validate_question(self, value):
        import pdb
        pdb.set_trace()
        return value.lower()

