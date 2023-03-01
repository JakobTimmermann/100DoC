class Flat:

    def __init__(self, data):
        self._flat_data = data
        self._flat_info = self._flat_data.find(name="a", class_="detailansicht")
        self._extract_href()
        self._extract_label()
        self._extract_hard_facts()
        self._extract_address()
#        self.prompt_info()

    def _extract_href(self):
        self._href = "https://www.wg-gesucht.de/" + self._flat_info.attrs["href"]

    def get_href(self):
        return self._href

    def _extract_label(self):
        self._flat_label = self._flat_info.attrs["href"]

    def _extract_address(self):
        self._address = self._flat_data.find(class_="col-xs-11").find("span").text.strip().split('\n')[-1].strip()

    def get_address(self):
        return self._address

    def prompt_info(self):
        print(self.get_href())
        print(self.get_address())
        print(self.get_price())
        print(self.get_flat_size())

    def _extract_hard_facts(self):
        self._flat_facts = self._flat_data.find_all(class_="col-xs-3")
        for facts in self._flat_facts:
            if "€" in facts.text:
                self._price = facts.text.strip().split()[0]
            elif "m²" in facts.text:
                self._flat_size = facts.text.strip().split()[0]

    def get_price(self):
        return self._price

    def get_flat_size(self):
        return self._flat_size
