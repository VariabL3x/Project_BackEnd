from models.base_model import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True)
    password = pw.CharField(index=True)
    email = pw.CharField(unique=True,index=True)
    avatar_url = pw.TextField(null=True)

    def as_dict(self):
        json_obj = {
            'id' : self.id,
            'username':self.username,
            'email' : self.email,
            'avatar_url' : self.avatar_url,
        }

        return json_obj

