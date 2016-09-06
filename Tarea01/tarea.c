#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <pcap.h>
#include <arpa/inet.h>
#include "tarea.h"


#include<net/ethernet.h>
#include<netinet/ip_icmp.h>   
#include<netinet/udp.h>   
#include<netinet/tcp.h>   
#include<netinet/ip.h>   
#include<string.h> 


/*********************************************
 *  Correr usando  
 * gcc tarea.c -o tarea -lpcap
 *
 * ******************************************/
int opcionUnPaquete () {
     //Obtenemos interfaz disponible
     char errbuf[PCAP_ERRBUF_SIZE];
     char *dev;
     const struct ip_header *ip;
     pcap_t *captura;
     const u_char *paquete;
     struct pcap_pkthdr h;


     dev = pcap_lookupdev(errbuf);
     //Si el apuntador a dispositivo de red no es válido, no continuamos
     if(dev ==NULL) {
         printf("En dispositivo de red ERROR: %s\n", errbuf);
         return EXIT_FAILURE;
     }
     
     printf("Capturaremos del dispositivo: %s \n", dev);
     
     captura = pcap_open_live(dev,BUFSIZ,1,50000, errbuf);
     
     if(captura== NULL) {
         printf("En captura ERROR: %s\n", errbuf);
         return EXIT_FAILURE;
     }
     
     paquete = pcap_next(captura, &h);
     
     if(paquete == NULL) {
         printf("Al recibir un paquete ERROR: %s \n",errbuf);
         return EXIT_FAILURE;
     }
     printf("Imprimimos el paquete\n");
     int i;
     for(i = 0;i < h.len; i++) {
         printf("%x ", paquete[i]);
     }
     printf("\n");

     ip = (struct ip_header*)(paquete + TAM_ETHERNET);
     printf("\nIP Origen :(%x )%s -> IP destino :(%x)%s \n",ip -> ip_src, inet_ntoa(ip->ip_src),((*ip).ip_dst),inet_ntoa(ip->ip_dst));
     
     
     int var=ip->ip_p;
     printf("Protocolo :%x \n", ip->ip_p);    
     
      unsigned short iphdrlen;
    struct ethhdr *eth = (struct ethhdr *)paquete;
    struct iphdr *iph = (struct iphdr *)(paquete  + sizeof(struct ethhdr) );
    struct sockaddr_in source;
    iphdrlen =iph->ihl*16;
    
    memset(&source, 0, sizeof(source));
    source.sin_addr.s_addr = iph->saddr;
    
    printf("version : %d\n",(unsigned int)iph->version);
    printf("IP Header Length  : %d DWORDS or %d Bytes\n",(unsigned int)iph->ihl,((unsigned int)(iph->ihl))*4);
    
    printf("Service   : %d\n",(unsigned int)iph->tos);
    
    printf("Checksum : %d\n",ntohs(iph->check));
    
    printf("Source IP : %s\n" , inet_ntoa(source.sin_addr));
     

     return EXIT_SUCCESS;
 }
 
 int archivoP(){
     const u_char *paquete;
struct pcap_pkthdr h;


pcap_t *pcap_open_offline(const char *fname, char *errbuf);
char error_buffer[PCAP_ERRBUF_SIZE];
pcap_t *captura = pcap_open_offline("mipaquete2.pcap", error_buffer);
const struct ip_header *ip;

u_char ip_p; /* protocol */

if(captura != NULL){
    printf("\n");
    paquete = pcap_next(captura, &h);
    
}

    if(paquete==NULL){
        printf("error");
    }
    int i;
    for(i = 0;i < h.len; i++) {
         printf("%x ", paquete[i]);
         
        }
        printf("\n");
    ip = (struct ip_header*)(paquete + 14);
      int var=ip->ip_p;
      
    printf("\n protocol: %x \n",ip->ip_p);
    
    /***********************************************************************/
    
    unsigned short iphdrlen;
    struct ethhdr *eth = (struct ethhdr *)paquete;
    struct iphdr *iph = (struct iphdr *)(paquete  + sizeof(struct ethhdr) );
    struct sockaddr_in source;
    iphdrlen =iph->ihl*16;
    
    memset(&source, 0, sizeof(source));
    source.sin_addr.s_addr = iph->saddr;
    
    printf("version : %d\n",(unsigned int)iph->version);
    printf("IP Header Length  : %d DWORDS or %d Bytes\n",(unsigned int)iph->ihl,((unsigned int)(iph->ihl))*4);
    
    printf("Service   : %d\n",(unsigned int)iph->tos);
    
    printf("Checksum : %d\n",ntohs(iph->check));
    
    printf("Source IP : %s\n" , inet_ntoa(source.sin_addr));
return 0;
     
}

int main (){
    int opcion=0;
    
    printf("\tMENu \n");   
    printf("\t1: para capturar el paquete de red\n");
    printf("\t2: para abrir en paquete de red\n");
    
    printf("\n");
    fflush(stdout);
 
    scanf("%d",&opcion);
 
        if(opcion==1){
            opcionUnPaquete();
            
        }else{
            if(opcion==2 ){
                archivoP();
            }else{
                printf("opcion invalida\n");
            }
        }
    
 
 
  return 0;
}
