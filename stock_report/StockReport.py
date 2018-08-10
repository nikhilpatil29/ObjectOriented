#
class StockReport():

    # def __init(self,share_name,share_number,share_prize,total_prize):
    #     self.__shareName = share_name
    #     self.__noOfShare = share_number
    #     self.__sharePrize = share_prize
    #     self.__shareTotal = total_prize

    def set_name(self,share_name):
        self.__shareName = share_name

    def set_no_of_share(self, no_of_share):
        self.__noOfShare = no_of_share

    def set_prize(self, prize):
        self.__sharePrize = prize

    def set_total(self, total):
        self.__shareTotal = total

    def get_name(self):
        return self.__shareName

    def get_no_of_share(self):
        return self.__noOfShare

    def get_prize(self):
        return self.__sharePrize

    def get_shareTotal(self):
        return self.__shareTotal


