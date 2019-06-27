''' frequency counter in python'''
def frequency_counter():
    freq={}
    words=input().split()
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    max_count=0
    max_word=''
    for (w,c) in freq.items():
        if c>max_count:
            max_word=w
            max_count=c
    print(max_word)
    print(max_count)
    #sorted_worddict=sorted((value,key) for (key,value) in freq.items())
    #print(sorted_worddict)
    #print(sorted_worddict[len(sorted_worddict)-1:])
class MapBase:
    ''' abstract class representing map base class'''
    def __setitem__(self,key,value):
        raise NotImplementedError('must be implemented by sub class')
    def __getitem__(self,key):
        raise NotImplementedError('must be implemented by sub class')
    def __len__(self):
        raise NotImplementedError('must be implemented by sub class')
    def __iter__(self):
        raise NotImplementedError('must be implemented by sub class')
    def __delitem__(self,key):
        raise NotImplementedError('must be implemented by sub class')
    class _item:
        __slot__='_key','_value'
        def __init__(self,key,value):
            self._key=key
            self._value=value
        def __eq__(self,other):
            return self._key==other._key
        def __ne__(self,other):
            return not(self==other)
        def __lt__(self,other):
            return self._key > other._key
class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table=[]
    def __getitem__(self,k):
        for item in self._table:
            if k==item._key:
                return item._value
            raise KeyError('key error :'+ repr(k))
    def __setitem__(self,k,v):
        for item in self._table:
            if k==item._key:
                item._value=v
        self._table.append(self._item(k,v))
    def __delitem__(self,k):
        for i in range(len(self._table)):
            if k == self._table[i].key:
                self._table.pop(i)
                return
        raise KeyError('KeyError:' +repr(k))
    def __len__(self):
        return len(self._table)
    def __iter__(self):
        for item in self._table:
            yield item._key
class HashMapBase(MapBase):
    def __init__(self,cap=11,p=109345121):
        self._table=cap*[None]
        self._n=0
        self._prime=p
        self._scale=1+ randrange(p-1)
        self._shift=randrange(p)
    def _hash_function(self,k):
        return (hash(k)*self._scale +self._shift) % self._prime % len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self,k):
        j=self._hash_function(k)
        return self._bucket_getitem__(j,k)
    def __setitem__(self,k,v):
        j=self._hash_function(k)
        self._bucket_setitem__(j,k,v)
        if self._n>len(self._table)//2:
            self._resize(2*len(self._table)-1)
    def __delitem__(self,k):
        j=self._hash_function(k)
        self._bucket_delitem(j,k)
        self._n-=1
class ChainHashMap(HashMapBase):
    '''hashtable implemented with sepreate chaining for collision resolution'''
    def _bucket_getitem__(self,j,k):
        bucket=self._table[j]
        if bucket is None:
            raise KeyError('key Error' + repr(k))
        return bucket[k]
    def _bucket_setitem__(self,j,k,v):
        if self._table[j] is None:
            self._table[j]=UnsortedTableMap()
            oldsize=len(self._table[j])
            self._table[j][k]=v
            if len(self._table[j])>oldsize:
                self._n +=1
    def _bucket_delitem(self,j,k):
        bucket=self._table[j]
        if bucket is None:
            raise KeyError('key Error' + repr(k))
        del bucket[k]
    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

''' binary search '''
def binarySearch(lis,target,low, high):
    if low > high:
        return False
    else:
        mid=(low+high)/2
        if target==lis[mid]:
            return True
        elif target < lis[mid]:
            return binraySearch(lis,target,low,mid-1)
        else:
            return binarySerach(lis,target,mid+1,high)
class SortedTableMap(MapBase):
    '''map implementation using a sorted behaviour'''
    def _findIndex(self,k,low,high):
        if high > low:
            return high+1
        else:
            mid=(low+high)/2
            if k==self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._findIndex(k,low,mid-1)
            else:
                return self._findIndex(k,mid+1,high)
        def __init__(self):
            self._table=[]
        def __len__(self):
            return len(self._table)
        def __getitem__(self,K):
            j=self._findIndex(k,0,len(self._table)-1)
            if j==len(self._table) or self._table[j]._key !=k:
                raise KeyError('Key Error' + repr(k))
            return self._table[j]._value
        def __setitem__(self,k,v):
            j=self._findIndex(k,0)
            if j < len(self._table) and K==self.table[j]._key:
                self._table[j]._value=v
            else:
                self._table.insert(j,self._item(k,v))
        def __delitem__(self,k):
            j=self._findIndex(k,0,len(self._table)-1)
            if j==len(self._table) and self._table[j]._key !=k:
                raise KeyError('key error' + repr(k))
            else:
                self._table.pop(j)
        def __iter__(self):
            for item in self._table:
                yield item._key
        def __reversed__(self):
            for item in reversed(self._table):
                yield item._key
        def




















if __name__=='__main__':
    #frequency_counter()
    map=UnsortedTableMap()
    map.__setitem__('arvind',10)
    map.__setitem__('python',20)
    print(map.__len__())
