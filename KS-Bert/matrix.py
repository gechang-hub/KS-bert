#coding='utf-8'
import seaborn as sns
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

sns.set()
f,ax = plt.subplots()
y_true = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]

y_pred =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 1, 1, 4, 6, 4, 1, 4, 4, 1, 7, 7, 5, 5, 7, 5, 5, 1, 1, 1, 1, 1, 1, 3, 1, 7, 1, 1, 2, 2, 1, 2, 2, 2, 6, 1, 2, 1, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 7, 2, 2, 2, 2, 2, 1, 1, 5, 6, 4, 5, 6, 1, 0, 7, 3, 4, 6, 7, 1, 1, 1, 1, 3, 6, 3, 3, 3, 3, 3, 5, 7, 3, 3, 2, 3, 3, 4, 4, 4, 4, 1, 4, 1, 4, 4, 7, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 4, 4, 7, 7, 1, 2, 3, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 7, 6, 3, 5, 5, 5, 3, 3, 6, 5, 7, 0, 5, 5, 6, 6, 6, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 1, 6, 2, 0, 6, 6, 6, 6, 6, 3, 5, 5, 5, 5, 5, 7, 4, 6, 1, 7, 7, 4, 7, 1, 1, 7, 3, 7, 5, 3, 7, 7, 7, 7, 7, 7, 5, 7, 7]

C2 = confusion_matrix(y_true,y_pred,labels=[0,1,2,3,4,5,6,7])
#打印 C2
print(C2)
sns.heatmap(C2,annot=True,ax=ax) #画热力图

ax.set_title('confusion matrix_tfidf') #标题
ax.set_xlabel('predict') #x 轴
ax.set_ylabel('true') #y 轴
plt.show()