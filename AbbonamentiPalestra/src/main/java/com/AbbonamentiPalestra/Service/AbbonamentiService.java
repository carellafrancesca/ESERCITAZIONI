package com.AbbonamentiPalestra.Service;

import java.time.LocalDate;
import java.time.Period;
import java.util.List;
import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;
import com.AbbonamentiPalestra.Repository.AbbonamentiRepo;

@Service
public class AbbonamentiService {

	Logger log = LoggerFactory.getLogger(AbbonamentiService.class);
	
	@Autowired AbbonamentiRepo abtr;
	
	@Autowired @Qualifier("abbonamenti") private ObjectProvider <Abbonamenti> abbonamentiProvider;
	
	public Abbonamenti registrazione(LocalDate dataDiIscrizione,TipoAttivita attivita, TipoAbbonamento tipo, Abbonati abbonato) {
		Abbonamenti abt = abbonamentiProvider.getObject();
	    abt.setDataDiIscrizione(dataDiIscrizione);
	    abt.setAttivita(attivita);
	    abt.setTipo(tipo);
	    abt.setAbbonato(abbonato);
	    
	    LocalDate dataDiScadenza = calcolaDataScadenza(dataDiIscrizione, tipo);
        abt.setDataDiScadenza(dataDiScadenza);
	    
        // Calcola il prezzo dinamicamente e imposta il campo prezzo dell'oggetto Abbonamenti
        double prezzoAbbonamento = abt.getPrezzo();
        abt.setPrezzo(prezzoAbbonamento);
	    
	    System.out.println(abt);
	    abtr.save(abt);
	    log.info(abbonato.getNome() + " " + abbonato.getCognome() + " si è registrato con abbonamento " + tipo + " al prezzo di " + prezzoAbbonamento);
	    return abt;
	}
	
    private LocalDate calcolaDataScadenza(LocalDate dataDiIscrizione, TipoAbbonamento tipo) {
        LocalDate dataDiScadenza = null;

        switch (tipo) {
            case MENSILE:
                dataDiScadenza = dataDiIscrizione.plus(Period.ofMonths(1));
                break;
            case SEMESTRALE:
                dataDiScadenza = dataDiIscrizione.plus(Period.ofMonths(6));
                break;
            case ANNUALE:
                dataDiScadenza = dataDiIscrizione.plus(Period.ofYears(1));
                break;
            default:
                break;
        }

        return dataDiScadenza;
    }
	
	public List<Abbonamenti> findAllAbbonamenti(){
		System.out.println("Lista di tutti gli abbonamenti:");
		return (List<Abbonamenti>) abtr.findAll();
	}
	
	public Abbonamenti findAbbonamentoById(Long id) {
	    return abtr.findById(id)
	            .orElseThrow(() -> new AbbonamentoNotFoundException("Abbonamento non trovato con ID: " + id));
	}
	
	public class AbbonamentoNotFoundException extends RuntimeException {
	    public AbbonamentoNotFoundException(String message) {
	        super(message);
	    }
	}

	public List <Abbonamenti> findAbbonamentiByTipo(TipoAbbonamento tipo) {
		System.out.println("Tipologia di Abbonamenti:" + tipo);
		return abtr.findByTipo(tipo);
	}
	
	public List <Abbonamenti> findAbbonamentiByAttivita(TipoAttivita attivita) {
		System.out.println("Tipologia di Attività:" + attivita);
		return abtr.findByAttivita(attivita);
	}
	
	public List<Abbonamenti> findAbbonamentiByNomeCognomeAbbonato(String nome, String cognome) {
        List<Abbonamenti> abbonamenti = abtr.findByAbbonatoNomeAndAbbonatoCognome(nome, cognome);
        if (abbonamenti.isEmpty()) {
            // Gestisci il caso in cui non sono presenti abbonamenti per l'abbonato con il nome e cognome specificati
            log.warn("Nessun abbonamento trovato per l'abbonato con nome: " + nome + " e cognome: " + cognome);
        }
        return abbonamenti;
    }

    public void modificaTipoAbbonamento(Long id, TipoAbbonamento nuovoTipo) {
        Optional<Abbonamenti> abbonamentoOptional = abtr.findById(id);

        if (abbonamentoOptional.isPresent()) {
            Abbonamenti abbonamento = abbonamentoOptional.get();
            
            if (nuovoTipo != null) {
                abbonamento.setTipo(nuovoTipo);
            }

            abtr.save(abbonamento);
            log.info("Tipo di abbonamento modificato per l'abbonamento con ID: " + id);
            
        } else {
            log.warn("Abbonamento non trovato con ID: " + id);
        }
    }

    public void modificaTipoAttivita(Long id, TipoAttivita nuovaAttivita) {
        Optional<Abbonamenti> abbonamentoOptional = abtr.findById(id);

        if (abbonamentoOptional.isPresent()) {
            Abbonamenti abbonamento = abbonamentoOptional.get();
            
            if (nuovaAttivita != null) {
                abbonamento.setAttivita(nuovaAttivita);
            }

            abtr.save(abbonamento);
            log.info("Tipo di attività modificato per l'abbonamento con ID: " + id);
            
        } else {
            log.warn("Abbonamento non trovato con ID: " + id);
        }
    }
	
	public void deleteAbbonamentiById(Long id) {
		System.out.println("Abbonamento annullato!");
		abtr.deleteById(id);
	}
	
}
