package com.AbbonamentiPalestra.Service;

import org.springframework.stereotype.Service;

import com.AbbonamentiPalestra.Class.TipoAbbonamento;
import com.AbbonamentiPalestra.Class.TipoAttivita;

@Service
public class TipologieService {

    public TipoAttivita[] getTipiAttivita() {
        return TipoAttivita.values();
    }

    public TipoAbbonamento[] getTipiAbbonamento() {
        return TipoAbbonamento.values();
    }
}
