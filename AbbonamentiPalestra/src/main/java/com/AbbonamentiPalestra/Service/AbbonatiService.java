package com.AbbonamentiPalestra.Service;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.ObjectProvider;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.Recensioni;
import com.AbbonamentiPalestra.Repository.AbbonatiRepo;
import com.AbbonamentiPalestra.Repository.RecensioneRepository;

@Service
public class AbbonatiService {

	Logger log = LoggerFactory.getLogger(AbbonatiService.class);
	
	@Autowired AbbonatiRepo abr;
	@Autowired RecensioneRepository recensioneRepo;
	
	@Autowired @Qualifier("abbonati") private ObjectProvider<Abbonati> abbonatiProvider;

	
	public Abbonati iscrizione(String nome, String cognome, String email, String numeroTelefono, String cittaDiNascita, LocalDate dataDiNascita) {
		Abbonati ab = abbonatiProvider.getObject();
		ab.setNome(nome);
		ab.setCognome(cognome);
		ab.setEmail(email);
		ab.setNumeroTelefono(numeroTelefono);
		ab.setCittaDiNascita(cittaDiNascita);
		ab.setDataDiNascita(dataDiNascita);
		
		System.out.println(ab);
		abr.save(ab);
		log.info(ab.getNome() + ab.getCognome() + " " + "è iscritto");
		return ab;
	}

	public List<Abbonati> findAllAbbonati() {
	    System.out.println("Lista di tutti gli abbonati.");
	    return (List<Abbonati>) abr.findAll();
	}
	
	public Abbonati findAbbonatiById(Long id) {
		System.out.println("Utente trovato!");
		return abr.findById(id).get();
	}
	
	public List<Abbonati> findAbbonatiByCittaDiNascita(String cittaDiNascita) {
		System.out.println("Abbonati nati a :" + " " + cittaDiNascita);
	    return abr.findByCittaDiNascita(cittaDiNascita);
	}
	
	public void deleteAbbonatoById(Long id) {
		System.out.println("Utente eliminato!");
		abr.deleteById(id);
	}
	
	public void aggiungiRecensione(Long abbonatoId, Recensioni recensione) {
	    Abbonati abbonato = abr.findById(abbonatoId)
	                           .orElseThrow(() -> new AbbonatoNotFoundException(abbonatoId));
	    recensione.setAbbonato(abbonato);

	    System.out.println("Recensione salvata con successo!");
	    recensioneRepo.save(recensione);
	}

	public class AbbonatoNotFoundException extends RuntimeException {
	    public AbbonatoNotFoundException(Long abbonatoId) {
	        super("Abbonato non trovato con ID: " + abbonatoId);
	    }
	}
	
	public List<Recensioni> recuperaRecensioniAbbonato(Long abbonatoId) {
        Optional<Abbonati> abbonatoOptional = abr.findById(abbonatoId);
        
        if(abbonatoOptional.isPresent()) {
        	Abbonati abbonato = abbonatoOptional.get();
        	return abbonato.getRecensioni();
        } else {
        	throw new AbbonatoNotFoundError("Abbonato non trovato con ID: " + abbonatoId);
        }
    }
	
	public class AbbonatoNotFoundError extends RuntimeException {
	    public AbbonatoNotFoundError(String message) {
	        super(message);
	    }
	}
	
	public void eliminaRecensione(Long recensioneId) {
	    recensioneRepo.deleteById(recensioneId);
	}
	
}
