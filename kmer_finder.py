#organizing the kmer functions into a class to refresh myself on object oriented patterns in python
class Kmer:
    
    #the propertied of a kmer the length, the number of strings identified and the resulting array
    Kmer_K = 0
    Kmer_Count = 0
    Kmer_Array = []
    
    #options for the kmer -- you can optionally sort the results and control case sensitivity
    Sorted = False
    CaseSensitive = False
    
    #init actually sets everything up
    def __init__(self,str, k):
        self.Kmer_K = k
        self.Kmer_Array = self.PatternFinder(str,k)
        self.Kmer_Count = len(self.Kmer_Array)
    
    #pattern finder actually builds the array
    def PatternFinder(self,str, k):
        new_array = []
        counter = len(str) - k
        for i in range(counter+1):
            new_array.append(str[i:i+k])
        if self.Sorted:
            new_array = new_array.sort()
        return new_array
    
    #print function so kmer can describe itself
    def Print(self):
        print('k-mer length:',self.Kmer_K,'  k-mer count:',self.Kmer_Count)
    
    #find returns a substring by index
    def Find(self,i):
        assert i > -1 
        assert i < len(self.Kmer_Array) 
        return self.Kmer_Array[i]
    
    #match finds all the indices of a specific kmer in the array
    def Match(self,search_mer):
        match_indices = []
        index = 0
        for mer in self.Kmer_Array:
            if not self.CaseSensitive:
                mer = mer.lower()
                search_mer = search_mer.lower()
            if mer == search_mer:
                match_indices.append(index)
            index+=1
        return match_indices

#This function is setup to meet HW requirements
def PatternFinder(str,index):
    new_kmer = Kmer(str,index)
    kmer_list = new_kmer.Kmer_Array[0]
    k=1
    while k < len(new_kmer.Kmer_Array):
        kmer_list = kmer_list + " , " + new_kmer.Kmer_Array[k]
        k+=1
    return kmer_list

#This function is setup to meet HW requirements
def PatternCount(str,srch):
    new_kmer = Kmer(str,len(srch))
    matchArray = new_kmer.Match(srch)
    return len(matchArray)

#test set to confirm HW function work as intended.
def test_kmer():
    #Some strings to practice with
    starting_string='ATCGCTCTCTCACGTGCTCCTATGCT'
    search_1='ATC' 
    search_2='CTC'
    search_3='GCTC'
    search_4='CT'
    string1='ATCGC'
    string2='AGTCCTCTCGAGACT'
    print("testing class setup")
    my_kmer = Kmer(starting_string,3)
    my_kmer.Print()
    print(my_kmer.Find(2))
    print(my_kmer.Match(search_2))
    assert PatternCount(starting_string, search_1) == 1
    assert PatternCount(starting_string, search_2) == 4
    assert PatternCount(starting_string, search_3) == 2
    assert PatternCount(starting_string, search_4) == 6
    print("Pattern count passed")
    assert PatternFinder(string1,2) == 'AT , TC , CG , GC'
    assert PatternFinder(string1,3) =='ATC , TCG , CGC'
    assert PatternFinder(string2,10) =='AGTCCTCTCG , GTCCTCTCGA , TCCTCTCGAG , CCTCTCGAGA , CTCTCGAGAC , TCTCGAGACT'
    print("Pattern finder passed")