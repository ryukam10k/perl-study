#!/usr/bin/perl
##!"C:\xampp\perl\bin\perl.exe" #windows(xampp�p)

#cokiee��
$COOKIENAME = "count";
#�ۑ����ԁi�b�j
$COOKIELIFE = 5;
#�K��񐔏��
$MAX_COUNT = 3;

$count = 0;

# cokiee�擾
foreach $pair (split(/;\s*/, $ENV{'HTTP_COOKIE'})) {
    my ($name, $cookie) = split(/=/, $pair);
    if($name eq $COOKIENAME) {
        $count = $cookie;
        last;
    }
}

# cokiee�쐬
$count++;
@mon = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
@wdy = qw(Sun Mon Tue Wed Thu Fri Sat);
$life = $COOKIELIFE;
($sec, $min, $hour, $day, $mon, $year, $wday) = gmtime(time + $life);
$expires = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT", $wdy[$wday], $day, $mon[$mon], $year + 1900, $hour, $min, $sec);

# HTML�o��
print "Content-type: text/html\n";
print "Set-Cookie: $COOKIENAME=$count; expires=$expires;\n\n";    #cokiee��������
print "<html>\n";
print "<head>\n";
print "<title>�K���</title>\n";
print "</head>\n";
print "<body>\n";
print " $count ��ڂ̃A�N�Z�X<br>\n";
if($count ge $MAX_COUNT) {
	print " $MAX_COUNT ��ȏ�̓A�N�Z�X�ł��܂���B$COOKIELIFE �b�҂��Ă���A�N�Z�X�������Ă��������B<br>";
} else {
	print "�悤�����I�I";
}
print "</body>\n";
print "</html>\n";

exit;
