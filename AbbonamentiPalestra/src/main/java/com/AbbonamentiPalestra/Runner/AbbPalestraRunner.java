package com.AbbonamentiPalestra.Runner;

import java.time.LocalDate;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;
import com.AbbonamentiPalestra.Service.AbbonamentiService;
import com.AbbonamentiPalestra.Service.AbbonatiService;

@Component
public class AbbPalestraRunner implements CommandLineRunner{

	@Autowired AbbonamentiService abts;
	@Autowired AbbonatiService abs;
	
	@Override
	public void run(String... args) throws Exception {
		System.out.println("Gestione Abbonamenti Runner...");
		
		// ABBONATI
		
		//Abbonati ab1 = abs.iscrizione("Francesca", "Carella", "c_fra@email.com", "123456789", "Milano", LocalDate.of(2000, 3, 29));
		//Abbonati ab2 = abs.iscrizione("Giuseppe", "Verdi", "verdig@email.com", "63856294001", "Roma", LocalDate.of(1996, 7, 12));
		//Abbonati ab3 = abs.iscrizione("Mario", "Rossi", "rossimario@email.com", "4698949718", "Bari", LocalDate.of(1990, 12, 5));
		//Abbonati ab4 = abs.iscrizione("Sara", "Bianchi", "sarabi@email.com", "987654321", "Firenze", LocalDate.of(2001, 5, 20));
		//Abbonati ab5 = abs.iscrizione("Ilaria", "Blasi", "blasilaria@email.com", "3682498204", "Roma", LocalDate.of(1994, 9, 17));
		//Abbonati ab6 = abs.iscrizione("Lorenzo", "Cavallo", "lorenzocav@email.com", "2650483566", "Bari", LocalDate.of(1999, 1, 30));
		//Abbonati ab7 = abs.iscrizione("Valerio", "Valeri", "valerioval@email.com", "4785902417", "Milano", LocalDate.of(1996, 7, 12));
		//Abbonati ab8 = abs.iscrizione("Martina", "Rosa", "martinarosa@email.com", "749928749", "Milano", LocalDate.of(1988, 4, 21));
		//Abbonati ab9 = abs.iscrizione("Mattia", "Neri", "nerimattia@email.com", "829947193", "Firenze", LocalDate.of(1995, 2, 25));
		//Abbonati ab10 = abs.iscrizione("Alessio", "Alessi", "alealessi@email.com", "3379383895", "Roma", LocalDate.of(1998, 11, 13));
		
		//Abbonati ab11 = abs.iscrizione("Marica", "Marti", "martina_m@email.com", "092649164782", "Bari", LocalDate.of(2000, 6, 27));
		//Abbonati ab12 = abs.iscrizione("Lucrezia", "Lucri", "l_lucrezia@email.com", "84629403711", "Roma", LocalDate.of(1997, 7, 1));
		//Abbonati ab13 = abs.iscrizione("Federica", "Cavallo", "fedecav@email.com", "856274621791", "Firenze", LocalDate.of(2000, 11, 23));
		//Abbonati ab14 = abs.iscrizione("Antonio", "Sgura", "sgura_anto@email.com", "174629596025", "Roma", LocalDate.of(2001, 10, 14));
		//Abbonati ab15 = abs.iscrizione("Elisabetta", "Lococciolo", "locElisabetta@email.com", "331637489239", "Firenze", LocalDate.of(1999, 9, 30));
		//Abbonati ab16 = abs.iscrizione("Andrea", "Marangi", "andreaMar@email.com", "29497274950", "Milano", LocalDate.of(1999, 2, 26));
		//Abbonati ab17 = abs.iscrizione("Dario", "Moccia", "mocciadario@email.com", "84765832940", "Firenze", LocalDate.of(1989, 8, 20));
		//Abbonati ab18 = abs.iscrizione("Gianmarco", "Tocco", "giammotocco@email.com", "95763726428", "Roma", LocalDate.of(1996, 5, 30));
		//Abbonati ab19 = abs.iscrizione("Sofia", "Fiorini", "sofiafiorini@email.com", "684397589246", "Roma", LocalDate.of(1996, 11, 16));
		//Abbonati ab20 = abs.iscrizione("Enrico", "Silvestrin", "enricos@email.com", "339447248941", "Milano", LocalDate.of(1989, 1, 11));
		
		// ABBONAMENTI
		
		//Abbonamenti abt1 = abts.registrazione(LocalDate.of(2023, 11, 20), TipoAttivita.FITNESS, TipoAbbonamento.MENSILE, ab1);
		//Abbonamenti abt2 = abts.registrazione(LocalDate.of(2023, 3, 11), TipoAttivita.YOGA, TipoAbbonamento.SEMESTRALE, ab2);
		//Abbonamenti abt3 = abts.registrazione(LocalDate.of(2023, 3, 11), TipoAttivita.YOGA, TipoAbbonamento.SEMESTRALE, ab3);
		//Abbonamenti abt4 = abts.registrazione(LocalDate.of(2023, 6, 25), TipoAttivita.CROSSFIT, TipoAbbonamento.MENSILE, ab4);
		//Abbonamenti abt5 = abts.registrazione(LocalDate.of(2023, 9, 30), TipoAttivita.SALA_PESI, TipoAbbonamento.ANNUALE, ab5);
		//Abbonamenti abt6 = abts.registrazione(LocalDate.of(2023, 11, 20), TipoAttivita.FITNESS, TipoAbbonamento.MENSILE, ab6);
		//Abbonamenti abt7 = abts.registrazione(LocalDate.of(2023, 3, 11), TipoAttivita.CROSSFIT, TipoAbbonamento.SEMESTRALE, ab7);
		//Abbonamenti abt8 = abts.registrazione(LocalDate.of(2023, 3, 11), TipoAttivita.FIT_BOX, TipoAbbonamento.SEMESTRALE, ab8);
		//Abbonamenti abt9= abts.registrazione(LocalDate.of(2023, 6, 25), TipoAttivita.YOGA, TipoAbbonamento.MENSILE, ab9);
		//Abbonamenti abt10 = abts.registrazione(LocalDate.of(2023, 9, 30), TipoAttivita.SALA_PESI, TipoAbbonamento.ANNUALE, ab10);
			
		//Abbonamenti abt11 = abts.registrazione(LocalDate.of(2023, 12, 4), TipoAttivita.PILATES, TipoAbbonamento.MENSILE, ab11);
		//Abbonamenti abt12 = abts.registrazione(LocalDate.of(2023, 10, 30), TipoAttivita.YOGA, TipoAbbonamento.SEMESTRALE, ab12);
		//Abbonamenti abt13 = abts.registrazione(LocalDate.of(2023, 3, 19), TipoAttivita.FIT_BOX, TipoAbbonamento.ANNUALE, ab13);
		//Abbonamenti abt14 = abts.registrazione(LocalDate.of(2023, 7, 25), TipoAttivita.CROSSFIT, TipoAbbonamento.MENSILE, ab14);
		//Abbonamenti abt15 = abts.registrazione(LocalDate.of(2023, 9, 10), TipoAttivita.SALA_PESI, TipoAbbonamento.MENSILE, ab15);
		//Abbonamenti abt16 = abts.registrazione(LocalDate.of(2023, 11, 20), TipoAttivita.FITNESS, TipoAbbonamento.SEMESTRALE, ab16);
		//Abbonamenti abt17 = abts.registrazione(LocalDate.of(2023, 6, 12), TipoAttivita.PILATES, TipoAbbonamento.MENSILE, ab17);
		//Abbonamenti abt18 = abts.registrazione(LocalDate.of(2023, 5, 27), TipoAttivita.FIT_BOX, TipoAbbonamento.SEMESTRALE, ab18);
		//Abbonamenti abt19= abts.registrazione(LocalDate.of(2023, 12, 25), TipoAttivita.YOGA, TipoAbbonamento.MENSILE, ab19);
		//Abbonamenti abt20 = abts.registrazione(LocalDate.of(2023, 1, 18), TipoAttivita.SALA_PESI, TipoAbbonamento.ANNUALE, ab20);
		
		// TROVARE TUTTI GLI ABBONAMENTI E GLI ABBONATI
		
		//List <Abbonati> listaAbbonati = abs.findAllAbbonati();
	    //listaAbbonati.forEach(abb -> System.out.println(abb));

		//List <Abbonamenti> listaAbbonamenti = abts.findAllAbbonamenti();
		//listaAbbonamenti.forEach(abbonamenti -> System.out.println(abbonamenti));
		
		// MODIFICA UN ABBONAMENTO
		
		//abts.modificaTipoAbbonamento((long) 7, TipoAbbonamento.MENSILE);
	
		// ELIMINA ABBONAMENTI E ABBONATI
		
		//abs.deleteAbbonatoById((long) 11);
		
	}

}
