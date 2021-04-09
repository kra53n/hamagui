#!/bin/sh

HAMACHI_DST=/opt/logmein-hamachi

if [ -x /opt/logmein-hamachi/uninstall.sh ] ; then
	echo Removing previous version ..
	/opt/logmein-hamachi/uninstall.sh
fi

echo Copying files into $HAMACHI_DST ..
mkdir -p "$HAMACHI_DST/bin"
install -m 755 hamachid "$HAMACHI_DST/bin"
install -m 755 dnsup "$HAMACHI_DST/bin"
install -m 755 dnsdown "$HAMACHI_DST/bin"
install -m 755 uninstall.sh "$HAMACHI_DST"
install -m 444 README "$HAMACHI_DST"
install -m 444 LICENSE "$HAMACHI_DST"
install -m 444 CHANGES "$HAMACHI_DST"

echo Creating LogMeIn Hamachi symlink ..
ln -sf "$HAMACHI_DST/bin/hamachid" /usr/bin/hamachi

if [ ! -x /dev/net/tun ] ; then
	echo Creating TunTap ..
	mkdir -p /dev/net
	mknod /dev/net/tun c 10 200
	chmod 0666 /dev/net/tun
fi

echo Installing LogMeIn Hamachi service ..
install -m 755 hamachi-init /etc/init.d/logmein-hamachi


if [ -x /usr/lib/lsb/install_initd ] ; then
        /usr/lib/lsb/install_initd /etc/init.d/logmein-hamachi
elif [ -d /etc/rc0.d ] ; then
        ln -s /etc/init.d/logmein-hamachi /etc/rc0.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc1.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc2.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc3.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc4.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc5.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc6.d/K01logmein-hamachi
elif [ -d /etc/init.d/rc0.d ] ; then
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc0.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc1.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc2.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc3.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc4.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc5.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/init.d/rc6.d/K01logmein-hamachi
elif [ -d /etc/rc.d ] ; then
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc0.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc1.d/K01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc2.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc3.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc4.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc5.d/S01logmein-hamachi
        ln -s /etc/init.d/logmein-hamachi /etc/rc.d/rc6.d/K01logmein-hamachi
else
        echo "Cannot install hamachi autostart scripts."
fi


echo Starting LogMeIn Hamachi service ..
/etc/init.d/logmein-hamachi start

echo LogMeIn Hamachi is installed. See README for what to do next.
