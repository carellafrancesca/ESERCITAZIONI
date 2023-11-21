package com.AbbonamentiPalestra.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.AbbonamentiPalestra.Class.Abbonamenti;
import com.AbbonamentiPalestra.Class.Abbonati;
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
	
}
