def NWSeqAlign(seq1,seq2,gap_score=-1,match_score=1,mismatch_score=0):
  seq1,seq2 = list(seq1),list(seq2)

  #<======matrix formation=====>
  matrix = []
  for i in range (0,len(seq1)+1):
    k = []
    for j in range(0,len(seq2)+1):
      k.append(0)
    matrix.append(k) 

  #<=======Initiation============>
  for l in range(0,len(seq2)+1):
    matrix[0][l] = l*gap_score
  for m in range(1,len(seq1)+1):
    matrix[m][0] = m*gap_score

  #<======Matrix Filling=========>
  for row in range(1,len(seq1)+1):
    for column in range(1,len(seq2)+1):
      up,left,diag = 0,0,0
      
      up = matrix[row-1][column] + gap_score
      left = matrix[row][column-1] + gap_score
      if seq1[row-1] == seq2[column-1]:
        diag = match_score + matrix[row-1][column-1]
      else:
        diag = mismatch_score + matrix[row-1][column-1]
      matrix[row][column] = max(up,left,diag)

  #<=========Backtracing===========>
  

  
  return matrix
  
