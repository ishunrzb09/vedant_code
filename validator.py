
class logValidator():
    def __init__(self, json, log_string):
        self.json = json
        self.log_string = log_string

    def weekdaysValidator(self):
        if self.json == 'short':
            if str(self.log_string).lower() in ['mon','tue','wed','thu','fry','sat','sun']:
                return True
            else:
                return 'invalid day format from short check'
        elif self.json == 'long':
            if str(self.log_string).lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']:
                return True
            else:
                return 'invalid day format from long check'
        elif self.json == 'narrow':
            if str(self.log_string).lower() in ['m', 't', 'w', 'f', 's']:
                return True
            else:
                return 'invalid day format from narrow check'
        else:
            return 'invalid day format'