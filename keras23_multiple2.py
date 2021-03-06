from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

def split_sequence(sequence, n_steps):
    x, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence): # -1
            break
        seq_x, seq_y = sequence[i:end_ix,:-1], sequence[end_ix-1,-1]
        x.append(seq_x)
        y.append(seq_y)
    return array(x), array(y)

in_seq1 = array([10,20,30,40,50,60,70,80,90,100])
in_seq2 = array([15,25,35,45,55,65,75,85,95,105])
out_seq = array( [in_seq1[i] + in_seq2[i] for i in range(len(in_seq1))] )

print(in_seq1.shape) # (10, )
print(out_seq.shape) # (10, )

in_seq1 = in_seq1.reshape(len(in_seq1),1)
in_seq2 = in_seq2.reshape(len(in_seq2),1)
out_seq = out_seq.reshape(len(out_seq),1)

print(in_seq1.shape) # (10,1)
print(in_seq2.shape) # (10,1)
print(out_seq.shape) # (10,1)

from numpy import hstack
dataset = hstack((in_seq1, in_seq2, out_seq))
n_steps = 3

x, y = split_sequence(dataset, n_steps)

for i in range(len(x)):
    print(x[i], y[i])
    
#print(dataset)

print(x.shape)
print(y.shape)
'''
DNN이 2차원 데이터를 받기 때문에, 3차원 데이터인 X를 2차원 데이터로 reshape 함
LSTM이면 그대로 사용 가능하다
'''

# 실습
# 1. 함수 분석
# 2. DNN 모델 만들것
# 3. 지표는 loss
# 4. [[90, 95]
# 5. [100,105]
# 6. [110,115]] 215 predict

# LSTM
model = Sequential()
model.add(LSTM(32, activation='relu', input_shape=(3, 2))) 
# 10은 dense층
model.add(Dense(16))
model.add(Dense(8))
model.add(Dense(1))

#  
model.compile(optimizer='adam', loss='mse')
model.fit(x, y, epochs=100, batch_size=1, verbose=2)
 
x_input = array( [[90, 95], [100,105], [110,115]])
x_input = x_input.reshape((1,3,2))
 
yhat = model.predict(x_input)
print(yhat)
