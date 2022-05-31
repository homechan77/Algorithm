from collections import deque, defaultdict

def solution(m, musicinfos):
    # m을 
    mlist = []
    mqueue = deque(list(m))
    while mqueue:
        mpop = mqueue.popleft()
        if mpop == '#':
            mlist[-1] = mlist[-1]+'#'
        else:
            mlist.append(mpop)
            
    tmplist=[]
    for i in musicinfos:
        i = i.split(',')
        i[0] = i[0].split(':')
        i[1] = i[1].split(':')
        start = int(i[0][0])*60 + int(i[0][1])
        end = int(i[1][0])*60 + int(i[1][1])
        playtime = end-start # 재생시간
        
        title = i[2] # 노래 제목
        
        songcode = [] # 악보
        # '#'을 구분해 주기 위한 작업
        queue = deque(i[3])
        while queue:
            pop = queue.popleft()
            if pop == '#':
                songcode[-1] = songcode[-1]+'#'
            else:
                songcode.append(pop)

        if playtime <= len(songcode):
            songcode = songcode[:playtime]
        else:
            mok = playtime // len(songcode)
            nameoji = playtime % len(songcode)
            songcode = (songcode*mok)+songcode[:nameoji]
            
        tmplist.append([title, songcode, playtime])
    
    # 딕셔너리 형태로 key는 playtime(재생시간), value는 title(노래 제목)로 저장된다.
    answerdict=defaultdict(list)
    
    # m과 songcode(악보) 비교
    for j in tmplist:
        for k in range(len(j[1])):
            comparison = "".join(j[1][k:k+len(mlist)])
            if m == comparison:
                answerdict[j[2]].append(j[0])
                break
    
    # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
    # 조건이 일치하는 음악이 없을 때에는 “(None)”을 반환한다.
    if len(answerdict) == 0:
        return "(None)"
    else:
        return answerdict[max(answerdict.keys())][0]

        
m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
# return :"HELLO"