class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict()
        ##set our connections up, key is starting city, val is destination
        for key,val in paths:
            d[key] = val
            
       ##use a queue to search for the first vertex that isn't a starting city, start with first value in paths     
        q = [d[paths[0][0]]]
        
        ##repeat while our queue isn't empty
        while q:
            vertex = q.pop(0)
            ##check to see if vertex is a destination, if not, return.
            if vertex not in d:
                return vertex
            ##else we keep checking by adding the destination of our current city to queue
            else:
                q.append(d[vertex])