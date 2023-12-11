package com.AbbonamentiPalestra.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;
import com.AbbonamentiPalestra.Service.AbbonamentiService;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/abbonamenti")
public class AbbonamentiController {

	@Autowired private AbbonamentiService abbonamentoService;
	
	@GetMapping
	public List<Abbonamenti> getAllAbbonamenti(){
		return abbonamentoService.findAllAbbonamenti();
	}
	
	@GetMapping("/{id}")
	public Abbonamenti getAbbonamentiById(@PathVariable Long id) {
	    return abbonamentoService.findAbbonamentoById(id);
	}
	
	//Il parametro @RequestParam nei metodi del controller è utilizzato per estrarre i parametri dall'URL della richiesta HTTP. Quando stai cercando di filtrare gli abbonamenti per tipo o attività, è comune passare questi parametri attraverso l'URL
	
	@GetMapping("/tipo/{tipo}")
	public List<Abbonamenti> getAbbonamentiByTipo(@PathVariable TipoAbbonamento tipo) {
	    return abbonamentoService.findAbbonamentiByTipo(tipo);
	}
	
	@GetMapping("/attivita/{attivita}")
	public List<Abbonamenti> getAbbonamentiByAttivita(@PathVariable TipoAttivita attivita) {
	    return abbonamentoService.findAbbonamentiByAttivita(attivita);
	}
	
	@GetMapping("/abbonato/{nome}/{cognome}")
	public List<Abbonamenti> getAbbonamentiByNomeCognomeAbbonato(
	        @PathVariable String nome,
	        @PathVariable String cognome) {
	    return abbonamentoService.findAbbonamentiByNomeCognomeAbbonato(nome, cognome);
	}
	
	@PutMapping("/{id}/tipo")
	public void updateTipoAbbonamento (@PathVariable Long id, @RequestParam TipoAbbonamento tipo) {
		abbonamentoService.modificaTipoAbbonamento(id, tipo);
	}
	
	@PutMapping("/{id}/attivita")
	public void updateTipoAttivita(@PathVariable Long id, @RequestParam TipoAttivita attivita) {
		abbonamentoService.modificaTipoAttivita(id, attivita);
	}
	
	@DeleteMapping("/{id}")
	public void deleteAbbonamento(@PathVariable Long id) {
		abbonamentoService.deleteAbbonamentiById(id);
	}
	
}
