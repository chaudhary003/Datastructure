'''module containing priorty queue implementation'''
class PriortyQueueBase:
    '''Abstract class repsesenting base class for priorty queue'''
    class _item:
        __slot__='_key','_value'
        def __init__(self,key,value):
            self._key=key
            self._value=value
        def __lt__(self,other):
            return self._key < other._key
    def is_empty(self):
        return len(self)==0
