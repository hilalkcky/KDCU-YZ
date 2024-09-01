## Yapay Zeka ile Kodlama Dillerini Çeviren Uygulama
# Acıkhack2024TDDİ
Bu proje, yapay zeka tekniklerini kullanarak farklı programlama dilleri arasındaki çevirileri kolaylaştırmayı amaçlayan açık kaynaklı bir uygulamadır. Özellikle Java ve C# dilleri arasındaki karşılıklı çeviriler için optimize edilmiştir.

# Temel Özellikler:

Seq2Seq Modeli: Modelin omurgasını oluşturan Seq2Seq modeli, girdi olarak verilen bir kod bloğunu hedef dildeki eşdeğerine dönüştürmek için eğitilmiştir.  
Noktalama Düzeltme: Random Forest algoritması ile eğitilen bir model, üretilen kodun doğru noktalama işaretleriyle biçimlendirilmesini sağlar. Bu model, noktalama işaretli ve işaretsiz kod örneklerinden oluşan geniş bir veri seti üzerinde eğitilmiştir.  
Streamlit Arayüzü: Kullanıcı dostu bir web arayüzü sayesinde, kullanıcılar kodlarını kolayca yükleyebilir ve çeviri işlemini başlatabilir.  
Java ve C# Desteği: Şu an için Java ve C# dilleri arasındaki çeviriler desteklenmektedir.  

# Gelecek Özellikler:

Daha Fazla Dil Desteği: Mevcut veri setini genişleterek, daha fazla programlama dilini desteklemek için modelin eğitilmesi planlanmaktadır.  
Kod Düzenleme: Kullanıcı tarafından girilen kodun, kod editörleri ve geri bildirim mekanizmaları aracılığıyla doğrulanması ve düzeltilmesi için özellikler eklenecektir.  

# Teknolojiler:

Seq2Seq: Dizi-dizili çeviri modeli  
Random Forest: Sınıflandırma ve regresyon algoritması  
Streamlit: Web uygulaması geliştirme framework'ü  

# Kullanım Alanları: 

Hızlı Prototip Oluşturma: Farklı dillerdeki kod örneklerini hızlıca incelemek ve anlamak  
Kod Migrasyonu: Mevcut bir kod tabanını farklı bir dile taşımak  
Öğrenme Amaçlı: Yeni bir programlama dili öğrenirken örnek kodları farklı dillere çevirerek anlamak  
