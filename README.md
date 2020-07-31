## DEEPCHECKER KÜTÜPHANESİ
### https://pypi.org/project/DeepChecker/
### https://github.com/umitylmz/DeepChecker
### DE-DA, Kİ ve Mİ düzeltmesi için yayınlamış olduğumuz DeepChecker kütüphanesini doğrudan pip ile yükleyebilirsiniz.
kütüphaneyi yüklemek için:
```bash
   pip install DeepChecker
```
Kullanabileceğiniz fonksiyonlar ve kullanımları:
> Correct fonksiyonları cümlenin doğru halini döndürmektedir.
> Check fonksiyonları ise cümlenin sigmoid fonksiyonundan gelen değeri ifade eder. 0'a yakın olması ayrı yazılması gerektiğini göstermektedir
```py
from DeepChecker import correct_de, correct_ki, correct_mi, check_de, check_ki, check_mi 

print(correct_de("bu yaz bizimkiler x tatile gelecek")) # doğru hali output olarak gelecek
print(check_de("bu yaz bizimkiler x tatile gelecek") # sigmoid değeri output olarak dönecek
```
## DE/-DA İÇİN LİTERATÜR KARŞILAŞTIRMASI

| Yapılan Çalışmalar | Doğruluk Oranı |F1 Score|
| ------ | ------ | ------ |
| Fixy |%92.13|%92.23|
| Boğaziçi | %76.48 |%86.67|
| Google Docs | %34 |%--|
| Microsoft Office  |%29|%--|
| ITU | %0 |%--|
| Libra Office | %0 |%--|

Kullanılan metodoloji tamamiyle özgündür ve Literatürdeki diğer çalışmalardan farklı bir yaklaşıma dayanmaktadır. Performans sonuçları yaklaşımın doğruluğunu ispatlar niteliktedir.


# DE-DA Düzeltici

> - Accuracy on Test Data: 92.13%
> - ROC AUC on Test Data: 0.921

Confusion Matrix
[336706  20522]
[ 36227 327591]

| class | precision | recall | f1-score  |support
| ------ | ------ | ------ | ------ |------ |
| 0 | 0.9049 | 0.9397 | 0.9219 |357228
| 1 |  0.9384 |  0.9030 |0.9204|363818

Data
Oluşturulan 3605229 satır veri içeren etiketli -ki veriseti linki: 
[Data](https://drive.google.com/file/d/1HLA9z1QoLMQsni70riq8APj0Gp_2nMmg/view?usp=sharing)

# Kİ Düzeltici

> - Accuracy on Test Data: 91.32%
> - ROC AUC on Test Data: 0.913

Confusion Matrix
 [27113  3311]
 [ 1968 28457]

| class | precision | recall | f1-score  |support
| ------ | ------ | ------ | ------ |------ |
| 0 | 0.9323 | 0.8912 | 0.9113 |30424
| 1 |  0.8958 |  0.9353 |0.9151|30425

Oluşturulan 304244 satır veri içeren etiketli -ki veriseti linki: 
[Data](https://drive.google.com/file/d/1HLA9z1QoLMQsni70riq8APj0Gp_2nMmg/view?usp=sharing)


Oluşturulan 9507636 satır veri içeren etiketli -mi veriseti linki: 
[Data](https://drive.google.com/file/d/1vCPsqYSMLOFxCA1WeykVMx1fT-A8etlD/view?usp=sharing)


> - Accuracy on Test Data: 95.41%
> - ROC AUC on Test Data: 0.954

Confusion Matrix
[910361  40403]
[ 46972 903792]

| class | precision | recall | f1-score  |support
| ------ | ------ | ------ | ------ |------ |
| 0 | 0.9509 | 0.9575 |0.9542  | 950764
| 1 |  0.9572 |  0.9506 | 0.9539|950764

Literatürde ki ve mi ekleri üzerine yapılmış çalışmaya rastlanamaması projenin özgünlüğünü arttırmaktadır. 
