class Journal:
    """
    Represents the journal, where user can store and view thoughts
    Attrs: entries (dict of title:body)
    Methods:
        get_titles: returns titles (keys) as list
        get_title_str: returns formatted str of titles
        get_entry: takes title, returns body as string
        get_entry_str: takes title, returns formatted str of title and body
        write_entry: takes title and body, creates new entry if title not taken,
                    overrides old body if title exists
        delete_entry: takes title, deletes entry
    """

    def __init__(self):
        self.__entries = {}

    def get_titles(self):
        return list(self.__entries.keys())

    def get_title_str(self):
        output_str = ''
        for title in self.__entries.keys():
            output_str += f'* {title}\n'
        return output_str

    def get_entry(self,title):
        return self.__entries.get(title)

    def get_entry_str(self,title):
        body = self.__entries.get(title)
        if not body:
            return None
        else:
            return f'*** {title} ***\n{body}'

    def write_entry(self, title, body):
        self.__entries[title] = body

    def delete_entry(self,title):
        try:
            return self.__entries.pop(title)
        except KeyError:
            return None
