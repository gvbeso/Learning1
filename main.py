from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch, ThreeLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons

from datetime import datetime

from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from  kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from baza import Baza
db = Baza()



class Dialogcontent(BoxLayout):
    def __init__(self):
        super(Dialogcontent, self).__init__()
        self.ids.labeldate.text= str(datetime.now().strftime("%d-%m-%Y"))

    def on_save(self, instance, value, date_range):
        print(value)
        self.ids.labeldate.text=str(value)

    def on_dismiss(self):
        print("dismisss")

    def on_cancel(self, instance, value):
        print("cancel")
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")

    def EditTokaitme(self, item):
        app = MDApp.get_running_app()
        app.show_alert_dialog(item)

    def __init__(self, **kwargs):
        super(ListItemWithCheckbox, self).__init__(**kwargs)


        self.edit_button = MDIconButton(icon='pencil', on_release=lambda x: self.EditTokaitme(self))
        self.add_widget(self.edit_button)



class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")
    def DeleteTokaitme(self,item):


        self.parent.remove_widget(item)




class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom right container.'''

class Note(MDApp):
    dialog = None
    def build(self):
        return Builder.load_file('kv.kv')


    def on_start(self):

        data = db.outdata()
        for elem in data:

            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=elem[1]+" "+elem[2], secondary_text=elem[3], tertiary_text=str(elem[0]), icon='delete')
            )






    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls = Dialogcontent(),

            )
        self.dialog.open()

    def dialog_save(self,note,desc,date,rec):
        if note.text!='' and desc.text!='':


            icons = list(md_icons.keys())
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=note.text, secondary_text=desc.text,tertiary_text=date.text,icon='delete')
            )


            db.insertDB(note.text,desc.text,date.text)

            note.text=''
            desc.text=''
            date.text= str(datetime.now().strftime("%d-%m-%Y"))
            self.dialog_cancel()
        else:
            rec.text='Fields Are Required'



    def dialog_cancel(self):
        self.dialog.dismiss()

if __name__== '__main__':
    Note().run()


