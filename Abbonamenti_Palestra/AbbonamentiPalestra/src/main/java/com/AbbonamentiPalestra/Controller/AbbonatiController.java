package com.AbbonamentiPalestra.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
import com.AbbonamentiPalestra.Class.Recensioni;
import com.AbbonamentiPalestra.Repository.RecensioneRepository;
import com.AbbonamentiPalestra.Service.AbbonatiService;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/abbonati")
public class AbbonatiController {

	@Autowired private AbbonatiService abbonatiService;
	
	@GetMapping
	public List<Abbonati> getAllAbbonati(){
		return abbonatiService.findAllAbbonati();
	}
	
	@GetMapping("/{id}")
	public Abbonati getAbbonatiById(@PathVariable Long id) {
	    return abbonatiService.findAbbonatiById(id);
	}
	
	@GetMapping("/citta-di-nascita/{cittaDiNascita}")
	public List<Abbonati> getAbbonatiByCittaDiNascita(@PathVariable String cittaDiNascita) {
	    return abbonatiService.findAbbonatiByCittaDiNascita(cittaDiNascita);
	}
    
    @PostMapping("/{id}/recensioni")
    public ResponseEntity<String> aggiungiRecensione(@PathVariable Long id, @RequestBody Recensioni recensione) {
    	abbonatiService.aggiungiRecensione(id, recensione);
    	return ResponseEntity.ok("Recensione aggiunta con successo!");
    }

    @GetMapping("/{id}/recensioni")
    public ResponseEntity<List<Recensioni>> recuperaRecensioni(@PathVariable Long id) {
        List<Recensioni> recensioni = abbonatiService.recuperaRecensioniAbbonato(id);
        return ResponseEntity.ok(recensioni);
    }

    @DeleteMapping("/recensioni/{id}")
    public ResponseEntity<String> eliminaRecensione(@PathVariable Long id) {
        abbonatiService.eliminaRecensione(id);
        return ResponseEntity.ok("Recensione eliminata con successo!");
    }
	
}
