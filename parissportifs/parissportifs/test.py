import django
django.setup()
from app.mesparis.models import Paris,Bet,Trade
from django.utils import timezone

if __name__=='__main__':
    print "hello world"
    plist=Paris.objects.all()
    print plist
    #Paris manipulation    
    p1=Paris(text="Djokovic to win RG",category="tennis",pub_date=timezone.now())
    p1.save()
    p2=Paris(text="Federer to win RG",category="tennis",pub_date=timezone.now())
    p2.save()
    plist=Paris.objects.all()
    print plist
    p2=Paris.objects.get(id=1)
    print p2
    p2.pub_date=timezone.now()
    p2.save()
    qlist=Paris.objects.filter(text__startswith='Federer')
    qlist.delete()
    print Paris.objects.all()
    #putting some market
    print p2
    p2.bet_set.all()
    p2.bet_set.create(bid =45.00,bid_size=2,ask=50.00,ask_size=2,login ='drebou')
    p2.bet_set.create(bid =44.00,bid_size=2,ask=48.00,ask_size=2,login ='cderou')
    p2.bet_set.create(bid =46.00,bid_size=1,ask=49.00,ask_size=1,login ='mdeleu')
    b= p2.bet_set.get(id=1)
    print b.paris
    print p2.bet_set.count()
    p2.bet_set.all().delete()



